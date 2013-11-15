#!/usr/bin/env python

import os
import re

# Compile a regex for faster searching
re_distrofile = re.compile ('BackTrack.+')


def get_version():
    readversion=file("bin/version/version","r")
    for line in readversion:
        version=line.rstrip()
    return version


def print_banner():
    os.system("clear")
    print ''' *****************************************************************
 **                                                             **
 **  Fast-Track - A new beginning...                            **
 **  Version: 4.0.2                                             **
 **  Written by: David Kennedy (ReL1K)                          **
 **  Lead Developer: Joey Furr (j0fer)                          **
 **  http://www.secmaniac.com                                   **
 **                                                             **
 *****************************************************************'''
 
