from common_core.settings import Config
import time

def timeit(func):
    """
    Decorator function to measure duration of each event (http request)
    """

    def wrapper_func(*args, **kwargs):
        t0 = time.time()
        resp = func(*args, **kwargs)
        duration_ms = (time.time() - t0) * 1000

        if kwargs.get('endpoint'):
            endpoint_full = kwargs.get('endpoint')
        else:
            endpoint_full = args[1]

        info = {
            # 'stack_trace': parse_stack_trace(inspect.stack()),
            'endpoint_full': endpoint_full,
            'request': {
                'payload': None
            },
            'response': {
                'status_code': resp.status_code,
                'url': getattr(resp, 'url', None),
            },
        }

        # if Config.CAPTURE_PAYLOAD and kwargs.get('data'):
        #     try:
        #         payload = json.loads(kwargs.get('data'))
        #     except Exception:
        #         payload = kwargs.get('data')
        #     info['request'].update({
        #         'payload': payload,
        #         })
        # if Config.CAPTURE_RESPONSE:
        #     info['response'].update({
        #         'json_response': resp.json_response,
        #         })

        # save_to_db(
        #     rtype=func.__name__,
        #     ep_name=kwargs.get('ep_name') or 'unk',
        #     duration=duration_ms,
        #     info=info
        #     )
        return resp

    def _func(*args, **kwargs):
        resp = func(*args, **kwargs)
        return resp

    # if Config.CAPTURE_RESULTS:
    #     return wrapper_func
    # else:
    #     return _func
