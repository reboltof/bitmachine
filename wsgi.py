#!/usr/bin/env python3
# encoding: utf-8

# wsgi.py
# Created by xtof on 06/08/2018.

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	return ['<!DOCTYPE html><html><meta charset="utf-8"><title>It works','</title><h1>It works!</h1>']
#	return['ok']

