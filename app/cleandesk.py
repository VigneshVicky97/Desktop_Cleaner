from pathlib import Path
from time import sleep

from watchdog.observers import Observer

from EventHandler import EventHandler

if __name__ == '__main__':
    watch_path_1 = Path.home() / 'Downloads'
    watch_path_2 = Path.home() / 'Pictures'
    watch_path_3 = Path.home() / 'Desktop'
    destination_root_1 = Path.home() / 'Downloads/holder of things'
    destination_root_2 = Path.home() / 'Pictures/holder of things'
    destination_root_3 = Path.home() / 'Desktop/holder of things'

    event_handler_1 = EventHandler(watch_path=watch_path_1, destination_root=destination_root_1)
    event_handler_2 = EventHandler(watch_path=watch_path_2, destination_root=destination_root_2)
    event_handler_3 = EventHandler(watch_path=watch_path_3, destination_root=destination_root_3)

    observer_1 = Observer()
    observer_1.schedule(event_handler_1, f'{watch_path_1}', recursive=True)
    observer_1.start()

    observer_2 = Observer()
    observer_2.schedule(event_handler_2, f'{watch_path_2}', recursive=True)
    observer_2.start()

    observer_3 = Observer()
    observer_3.schedule(event_handler_3, f'{watch_path_3}', recursive=True)
    observer_3.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer_1.stop()
        observer_2.stop()
        observer_3.stop()
    observer_1.join()
    observer_2.join()
    observer_3.join()
