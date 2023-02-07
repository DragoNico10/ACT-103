import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler as FSEH
to_dir='test_dir'
if not os.path.exists(to_dir):
    print(f'Path {to_dir} does not exist!\nCreating path...')
    os.mkdir(to_dir)
class FileEventHandler(FSEH):
    def on_created(self, event):
        print(f'{event.src_path} was created!')
    def on_deleted(self, event):
        print(f'{event.src_path} was deleted!')
    def on_modified(self, event):
        print(f'{event.src_path} was modified!')
    def on_moved(self, event):
        print(f'{event.src_path} was moved to {event.dest_path}!')
handler=FileEventHandler()
observer=Observer()
observer.schedule(handler,to_dir,True)
observer.start()
try:
    print('Executing...')
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print('Execution stopped!')
    observer.stop()
