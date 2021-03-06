#!/usr/bin/env python

# psycopg2 test suite
#
# Copyright (C) 2007-2011 Federico Di Gregorio  <fog@debian.org>
#
# psycopg2 is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In addition, as a special exception, the copyright holders give
# permission to link this program with the OpenSSL library (or with
# modified versions of OpenSSL that use the same license as OpenSSL),
# and distribute linked combinations including the two.
#
# You must obey the GNU Lesser General Public License in all respects for
# all of the code used other than OpenSSL.
#
# psycopg2 is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

import os
import sys
from testconfig import dsn
from testutils import unittest

# If connection to test db fails, bail out early.
import psycopg2
try:
    cnn = psycopg2.connect(dsn)
except Exception, e:
    print "Failed connection to test db:", e.__class__.__name__, e
    print "Please set env vars 'PSYCOPG2_TESTDB*' to valid values."
    sys.exit(1)
else:
    cnn.close()

import bug_gc
import bugX000
import extras_dictcursor
import test_dates
import test_psycopg2_dbapi20
import test_quote
import test_connection
import test_cursor
import test_transaction
import types_basic
import types_extras
import test_lobject
import test_copy
import test_notify
import test_async
import test_green
import test_cancel

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(bug_gc.test_suite())
    suite.addTest(bugX000.test_suite())
    suite.addTest(extras_dictcursor.test_suite())
    suite.addTest(test_dates.test_suite())
    suite.addTest(test_psycopg2_dbapi20.test_suite())
    suite.addTest(test_quote.test_suite())
    suite.addTest(test_connection.test_suite())
    suite.addTest(test_cursor.test_suite())
    suite.addTest(test_transaction.test_suite())
    suite.addTest(types_basic.test_suite())
    suite.addTest(types_extras.test_suite())
    suite.addTest(test_lobject.test_suite())
    suite.addTest(test_copy.test_suite())
    suite.addTest(test_notify.test_suite())
    suite.addTest(test_async.test_suite())
    suite.addTest(test_green.test_suite())
    suite.addTest(test_cancel.test_suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
