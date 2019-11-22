#!/usr/bin/python3
"""
   BaseModel is the parent of all the future
   that contain common attributes
"""
from datetime import datetime, date
import uuid
import models


class BaseModel():
    """
       Definition of the behavior of Base Model
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of the differents attributes of base model:

        Args:
             *args: Receive the arguments in list
             **kwargs: Receive the argumenst in form of keyword
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    object = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, object)
                elif key != "__class__":
                    setattr(self, key, value)
    
    def __str__(self):
        """
            Description of the class [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, str(self.__dict__))

    def save(self):
        """
           Update the public instance update_at
           with the current_time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
           Returns:
                 Dictionary with key and values of instance
        """
        d = {}

        for k, v in self.__dict__.items():
            d["__class__"] = self.__class__.__name__
            if k == "created_at" or k == "updated_at":
                d[k] = v.isoformat()
            else:
                d[k] = v
        return d
