service_name = data.get('service')
service_data = {k: v for k, v in data.items() if v}
service_data.pop('service', None)
service_data.pop('webhook_id', None)
if service_name is not None:
    domain, service = service_name.split('.')
    hass.services.call(domain, service, service_data, False)