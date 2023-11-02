#!/usr/bin/env bash
#
# Exaplanation: Test Logstash stages of the pipeline
#
# Usage:
#    $ bash  logstash_pipeline_test.bash [ stage ] [ input ] [ output ]
#
# Style:
#    Google Bash Style Guide:
#    https://google.github.io/styleguide/shellguide.html
#
#    @name           logstash_pipeline_test.bash
#    @version        1.00
#    @author-name    Wayne Kirk Schmidt
#    @author-email   wayne.kirk.schmidt@changeis.co.jp
#
umask 022

export PATH="/usr/share/logstash/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:$PATH"

### Define the bin and the etc directory as related to the running script
BINDIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
ETCDIR=$( realpath "$BINDIR"/../etc )

PipelineStage=${1:-"stage01"}
InputType=${2:-"syslog"}
OutputType=${3:-"stdout"}

DumpConfig="$ETCDIR/logstash.${PipelineStage}.${InputType}.${OutputType}.txt"

echo "timeout 12 logstash -f ${DumpConfig} --path.settings=/etc/logstash --log.level=fatal"
