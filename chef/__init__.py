# Copyright (c) 2010 Noah Kantrowitz <noah@coderanger.net>

__version_info__ = (0, 2, 1)
__version__ = '.'.join([str(x) for x in a])

from chef.api import ChefAPI, autoconfigure
from chef.client import Client
from chef.data_bag import DataBag, DataBagItem
from chef.exceptions import ChefError
from chef.node import Node
from chef.role import Role
from chef.environment import Environment
from chef.search import Search
