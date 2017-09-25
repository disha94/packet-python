# -*- coding: utf-8 -*-


class Hardware_Reservation():
    def __init__(self, data, manager):
        self.id = data['id']
        self.provisionable = data['provisionable']
        self.facility = data['facility']['href'].split('/')[2]
        self.plan = data['plan']['slug']

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
