from wsgiref.simple_server import make_server
from .app import application


def _parse_command_line_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname")
    parser.add_argument("port", type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_command_line_args()

    with make_server(args.hostname, args.port, application) as httpd:
        print(f"Serving on port {args.port}... (Use Ctrl-C to exit)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass