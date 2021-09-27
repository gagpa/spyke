def get_containers(client, *container_names):
    """Получить контейнеры"""
    all_containers = client.containers.list()
    if container_names:
        target_containers = list(filter(lambda container: container.name in container_names, all_containers))
    else:
        target_containers = all_containers
    return target_containers


def get_container(client, identify_sign: str):
    return client.containers.get(identify_sign)


def scan_container(client, model):
    """Просканировать инофрмацию о контейнерах"""
    container = get_container(client, model.name)
    return {
        'name': container.name,
        'status': container.status,
        'image': container.image.tags,
    }


def status_is_changed(model, scan_data):
    """Проверить измеение статуса"""
    return model.curr_status != scan_data['status']
