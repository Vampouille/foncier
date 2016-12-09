# -*- coding: utf-8 -*-
class BaseConfig(object):
    # General config
    DEBUG = True
    ROLE_PREFIX = 'ROLE_FONCIER_'
    FONCIER_EXTRACTS_DIR = '/tmp'
    # LDAP-related keys:
    LDAP_URI = 'ldap://localhost:10389'
    LDAP_BINDDN = 'cn=admin,dc=georchestra,dc=org'
    LDAP_PASSWD = 'secret'
    LDAP_ORGS_BASEDN = 'ou=orgs,dc=georchestra,dc=org'
    LDAP_SEARCH_FILTER = '(&(cn=%s)(objectClass=groupOfMembers))'
