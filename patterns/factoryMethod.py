# https://realpython.com/factory-method-python/

import xml.etree.ElementTree as et
import json
import yaml


class Song:
    """объект который хотим сериализовать в разных форматах"""

    def __init__(self, song_id, title, artist, year=None):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.year = year if year else 'Not added'

    def serialize(self, serializer):
        """методо среиализации"""
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)
        serializer.add_property('year', self.year)


class JsonSerializer:
    """JSON сериализатор (concrete creator)
    создаёт JSON представление объекта

    """

    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    """XML сериализатор (concrete creator)
    создаёт XML представление объекта

    """

    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


class YamlSerializer(JsonSerializer):
    """YAML сериализатор (concrete creator)
    создаёт YAML представление объекта

    """

    def to_str(self):
        return yaml.dump(self._current_object)


class SerializerFactory:
    """фабрика сериализаторов (creator)
    регистрирует/возвращает конкретную реализацию сериализатора

    """

    _creators = {}

    def register_format(self, format, creator):
        format = str(format).lower()
        if not self._creators.get(format):
            self._creators[format] = creator
        else:
            print(f'Формат {format} уже зарегистрирован')

    def get_serializer(self, format):
        format = str(format).lower()
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


class ObjectSerializer:
    """объектаная фабрика
    взаимодействует и с фабрикой сериализаторов и с объектом
    получает конкретный сериализатор через обращение к фабрике сериалиаторов (по формату)
    передает сериализатор в метод сериализации объекта

    """

    def serialize(self, serializable, format):
        serializer = SerializerFactory().get_serializer(format) # concrete serializer object
        serializable.serialize(serializer)
        return serializer.to_str()



def main():
    # регистрируем форматы в фабрике сериализаторов
    SerializerFactory().register_format('JSON', JsonSerializer)
    SerializerFactory().register_format('XML', XmlSerializer)
    SerializerFactory().register_format('YAML', YamlSerializer)

    # создаем объект песни
    song = Song('1', 'Water of Love', 'Dire Straits', '1985')

    # создаем объектную фабрику, которая внутри метода .serialize будет обращаться
    # к SerializerFactory и брать сериализатор согласно переданному формату
    serializer = ObjectSerializer()

    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))



if __name__ == '__main__':
    main()