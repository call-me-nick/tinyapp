#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--days",
        help="Days to display. (default: 40)",
        type=int,
        default=40
    )
    return parser.parse_args()


def main():
    args = cli()
    today = datetime.today()
    for from_now in reversed(range(0, args.days)):
        this_date = today + timedelta(days=from_now)
        print('## {}'.format(this_date.strftime('%Y.%m.%d - %a')))
        if this_date.strftime('%a') not in ['Sat', 'Sun']:
            print('  yesterday:\n  blockers:\n  today:\n  long-term:')


if __name__ == "__main__":
    main()
