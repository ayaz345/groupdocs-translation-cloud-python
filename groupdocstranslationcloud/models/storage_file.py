# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="storage_file.py">
# Copyright (c) 2022 GroupDocs.Translation for Cloud
# </copyright>
# <summary>
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

from groupdocstranslationcloud.models import BaseModel


class StorageFile(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'name': 'str',
        'is_folder': 'bool',
        'modified_date': 'datetime',
        'size': 'int',
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_folder': 'isFolder',
        'modified_date': 'modifiedDate',
        'size': 'size',
        'path': 'path'
    }

    def __init__(self, name=None, is_folder=None, modified_date=None, size=None, path=None):
        self._name = None
        self._is_folder = None
        self._modified_date = None
        self._size = None
        self._path = None

        if name is not None:
            self.name = name
        self.is_folder = is_folder
        if modified_date is not None:
            self.modified_date = modified_date
        self.size = size
        if path is not None:
            self.path = path

    @property
    def name(self):
        """Gets the name of this StorageFile.

        File or folder name.

        :return: The name of this StorageFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageFile.

        File or folder name.

        :param name: The name of this StorageFile.
        :type: str
        """

        self._name = name

    @property
    def is_folder(self):
        """Gets the is_folder of this StorageFile.

        True if it is a folder.

        :return: The is_folder of this StorageFile.
        :rtype: bool
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder):
        """Sets the is_folder of this StorageFile.

        True if it is a folder.

        :param is_folder: The is_folder of this StorageFile.
        :type: bool
        """
        if is_folder is None:
            raise ValueError("Invalid value for `is_folder`, must not be `None`")

        self._is_folder = is_folder

    @property
    def modified_date(self):
        """Gets the modified_date of this StorageFile.

        File or folder last modified DateTime.

        :return: The modified_date of this StorageFile.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this StorageFile.

        File or folder last modified DateTime.

        :param modified_date: The modified_date of this StorageFile.
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def size(self):
        """Gets the size of this StorageFile.

        File or folder size.

        :return: The size of this StorageFile.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this StorageFile.

        File or folder size.

        :param size: The size of this StorageFile.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size

    @property
    def path(self):
        """Gets the path of this StorageFile.

        File or folder path.

        :return: The path of this StorageFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this StorageFile.

        File or folder path.

        :param path: The path of this StorageFile.
        :type: str
        """

        self._path = path
