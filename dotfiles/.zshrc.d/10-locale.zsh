#
# ~/.zshrc.d/10-locale.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

if locale -a | grep -q "en_US.utf8"; then
    export LANG=en_US.UTF-8
    export LC_CTYPE=en_US.UTF-8
    export LC_COLLATE=en_US.UTF-8
    export LC_MESSAGES=en_US.UTF-8
else
    echo "locale en_US.utf8 not enabled"
fi

if locale -a | grep -q "de_CH.utf8"; then
    export LC_NUMERIC=de_CH.UTF-8
    export LC_MONETARY=de_CH.UTF-8
    export LC_PAPER=de_CH.UTF-8
    export LC_NAME=de_CH.UTF-8
    export LC_ADDRESS=de_CH.UTF-8
    export LC_TELEPHONE=de_CH.UTF-8
    export LC_MEASUREMENT=de_CH.UTF-8
    export LC_IDENTIFICATION=de_CH.UTF-8
else
    echo "locale de_CH.utf8 not enabled"
fi

if locale -a | grep -q "en_GB.utf8"; then
    export LC_TIME=en_GB.UTF-8
else
    echo "locale en_GB.utf8 not enabled"
fi
