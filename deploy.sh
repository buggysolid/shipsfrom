for machine in $(flyctl machines list | awk '/d+/ { print $1 }' | tail -n 2); do
    flyctl machine destroy --force $machine;
done

flyctl deploy
