# -*- coding: UTF-8 -*-


class HelloRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'db_blog':
            return 'db_blog'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'db_blog':
            return 'db_blog'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'db_blog' or \
            obj2._meta.app_label == 'db_blog':
            return True
        return None

    def allow_sysncdb(self, db, model):
        if db == 'db_blog' or model._meta.app_label == 'db_blog':
            return False
        else:
            return True