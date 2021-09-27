from time import sleep

import requests
import schedule
from loguru import logger
import docker
import app
from configs.bot import TOKEN

url_template = 'https://api.telegram.org/bot{}/sendMessage?chat_id=-{}&text={}'


@logger.catch()
def main():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    # client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
    container_models = app.container_entity.get_containers_to_scan()
    for i, model in enumerate(container_models):
        scan_data = app.docker_scaner.scan_container(client, model)
        if app.docker_scaner.status_is_changed(model, scan_data):
            app.container_entity.change_status(model, scan_data)
            requests.post(url_template.format(TOKEN, model.chat_id, f'Контейнер {model.label} - {scan_data["status"]}'))


if __name__ == '__main__':
    schedule.every(3).seconds.do(main)
    while True:
        schedule.run_pending()
        sleep(1)
