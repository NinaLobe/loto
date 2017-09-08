#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = 324
guess=int(raw_input("Ugani številko, je od 1 - 1000, imaš slabe možnosti...."))
if guess == secret:
    print "NORO, čestitam, kaj takega je 1:tisoč"
else:
    print("NE, NAROBE!")