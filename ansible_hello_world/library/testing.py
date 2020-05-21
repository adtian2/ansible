#! /bin/env python
from ansible.module_utils.basic import AnsibleModule
import os, json
import re, sys

def firstProg(text):
    text1 = "Hello " + text
    return text1

if __name__ == '__main__':
    fields = {
    "yourName": {"required": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)
    yourName = os.path.expanduser(module.params['yourName'])
    newName = firstProg(yourName)
    module.exit_json(msg=newName)
