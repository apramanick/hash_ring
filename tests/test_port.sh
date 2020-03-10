#!/usr/bin/env bash
#
# BSD 2-Clause License
#
# Copyright (c) 2020 Ankan Pramanick
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
