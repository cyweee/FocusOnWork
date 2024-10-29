#!/bin/bash

echo "script launch..."

while true; do
    echo "window checking..."
    # Печатаем все открытые окна
    wmctrl -l

    # Проверяем, есть ли окна с Instagram или YouTube
    if wmctrl -l | grep -E "Instagram|YouTube"; then
        echo "find windows from Instagram or YouTube, close..."
        # Закрываем окна
        wmctrl -c "Instagram"
        wmctrl -c "YouTube"
    else
        echo "no Instagram or YouTube windows were found."
    fi
    # checking every 5 sec
    sleep 5
done
