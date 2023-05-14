import argparse
from . import project_settings, dl_login, sync_images_to_dataloop, sync_annotations_to_dataloop

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ec2', action='store_true', help='Use this flag only if want to login on dataloop sdk using a bot account on ec2 instance')
    parser.add_argument('-images', action='store_true')
    parser.add_argument('-annotations', action='store_true')
    parser.add_argument('-dl_email', required=True)
    parser.add_argument('-dl_password', required=True)


    args = parser.parse_args()

    dl_login(args.ec2, args.dl_email, args.dl_password)

    if args.images:
        sync_images_to_dataloop(project_settings)
    if args.annotations:
        sync_annotations_to_dataloop(project_settings)

if __name__ == '__main__':
    main()