# -*- coding: utf-8 -*-

"""Console script for trade_mgr."""

import click
import click_completion
click_completion.init()


class AliasedGroup(click.Group):

    def list_commands(self, ctx):
        rv = ['bittrex', 'kraken']
        rv.sort()
        return rv

    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        print('rf: {}'.format(rv))
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))

@click.command(cls=AliasedGroup)
def main():
    pass

@main.command()
@click.argument('exchange')
def pairs(exchange):
    """Retrieve pairs"""
    print('Getting pairs for {}'.format(exchange))

@main.command()
@click.argument('exchange')
def wallets(exchange):
    """Retrieve wallets"""
    print('Getting wallets for {}'.format(exchange))

@main.command()
@click.argument('exchange')
@click.argument('pair')
def fetch(exchange, pair):
    """Retrieve pair information"""
    print('Getting pair {} from {}'.format(pair, exchange))


if __name__ == "__main__":
    main()
