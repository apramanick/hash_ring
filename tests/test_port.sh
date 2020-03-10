#!/usr/bin/env bash
#
# MIT License
#
# Copyright (c) 2020 Ankan Pramanick
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

# Quick sanity check for whether the Python 3.8 ported code gives the same output as
# the original Python 2.x code.  DO NOT USE IN LIEU OF A UNIT TEST SUITE!

print_help() {
  _PROGNAME=$( basename "$0" )
  echo "Usage: ${_PROGNAME} path-to-python2-interpreter path-to-python3-interpreter"
}

exit_help() {
  rc=$1
  message=$2
  if [[ -n $message ]]; then
    echo "$message"
  fi
  print_help
  exit "$rc"
}

# Main
[[ $# -eq 2 ]] || exit_help 2
PY2="$1"
PY3="$2"
[[ -x "$PY2" ]] || exit_help 1 "[error] Cannot execute '$PY2'"
[[ -x "$PY3" ]] || exit_help 1 "[error] Cannot execute '$PY3'"
PY2_OUT=py2.out
PY3_OUT=py3.out
rm -f $PY2_OUT $PY3_OUT
"$PY2" test_hash_ring_port.py 1>$PY2_OUT 2>&1
"$PY3" test_hash_ring_port.py 1>$PY3_OUT 2>&1
diff $PY2_OUT $PY3_OUT
RC=$?
if [[ $RC -ne 0 ]] ; then
  echo "Test FAILED! diff $PY2_OUT $PY3_OUT to see the difference in outputs."
  exit 1
else
  echo "Passed"
  rm -f $PY2_OUT $PY3_OUT
  exit 0
fi
