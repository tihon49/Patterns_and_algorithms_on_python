# SNMP

1. на сервере устанавливаем - пакеты 
    * `sudo apt-get install snmp`
    * `sudo apt-get install snmpd`
    * `sudo apt-get install libsnmp-dev`


2. на сервер добавить дефолтные OID в конфиг /etc/snmp/snmpd.conf (можно взять из комментов в http://jira.aerodisk.local:8080/browse/KBEN-645) и изменить `agentAddress`2 на `0.0.0.0`

3. на клиенте пакет snmp, для работы утилиты snmpwalk (она опрашивает сервер)
чтобы получить данные с сервера, то с клиента отправляем след.:

    v2:
    ```
    snmpwalk -v2c -c public 192.168.5.204 .1.3.6.1.4.1.54641.1.1
    ```

    v3:
    ```
    $ snmpwalk -v3 -u username -l authPriv -a MD5 -A "PASSWORD" -x DES -X "PASSWORD" 192.168.2.70 .1.3.6.1.4.1.2021.10.1.3.1
    ```

4. настройка community для SNMPv2 и сам SNMPv3 (логин + пароль) - http://wiki.aerodisk.local:8090/pages/viewpage.action?pageId=27232487

5. SNMPv3
на стороне сервера надо сначала создать пользователя, пример команды
net-snmp-create-v3-user -ro -a {} -x {} -X DES {}  # password, confirm_password, user_name

    на стороне клиента проверяем
    $ snmpwalk -v3 -u username -l authPriv -a MD5 -A "PASSWORD" -x DES -X "PASSWORD" 192.168.2.70 .1.3.6.1.4.1.2021.10.1.3.1

6. pass_persist
    ```
    #  ACCESS CONTROL
    #
    view   systemonly  included   .1.3.6.1.4.1.54641


    pass_persist    .1.3.6.1.4.1.54641.1     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/disks.py
    pass_persist    .1.3.6.1.4.1.54641.2     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/sensors.py
    pass_persist    .1.3.6.1.4.1.54641.3     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/rdg.py
    pass_persist    .1.3.6.1.4.1.54641.4     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/ddp.py
    pass_persist    .1.3.6.1.4.1.54641.5     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/ethernet.py
    pass_persist    .1.3.6.1.4.1.54641.6     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/smb.py
    pass_persist    .1.3.6.1.4.1.54641.7     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/nfs.py
    pass_persist    .1.3.6.1.4.1.54641.8     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/errors.py
    pass_persist    .1.3.6.1.4.1.54641.9     /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/fc.py
    pass_persist    .1.3.6.1.4.1.54641.10    /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/rdg_lun.py
    pass_persist    .1.3.6.1.4.1.54641.11    /usr/bin/sudo /var/engine/bin/SNMP/pass_persist/ddp_lun.py
    ```

Пример файла sensors.py

```python
#!/usr/bin/env python3
import snmp_passpersist as snmp
from LIB.a_functions import execute

def update():
    psu = execute("ipmitool sdr elist compact| grep PSU").split("\n")
    for i in range(len(psu)):
        name, code, status, volt, message = psu[i].split("|")
        pp.add_str('1.{0}'.format(i), name.strip())
        pp.add_str('2.{0}'.format(i), status.strip())
        pp.add_str('3.{0}'.format(i), message.strip() or "ready")
        pp.add_str('4.{0}'.format(i), code.strip())

pp=snmp.PassPersist(".1.3.6.1.4.1.54641.2")
pp.start(update,30) # Every 30s
```