#!/bin/bash

for build in {129..148}; do
    wget "https://ci.xwiki.org/view/Recommended%20Builds/job/xwiki-platform_pitest/$build/org.xwiki.platform\$xwiki-platform-webjars-api/consoleText" -O $build.txt
done
