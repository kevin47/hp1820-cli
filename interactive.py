from cmd import Cmd
import getpass
import cli

class Prompt(Cmd):
    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print("Hello, %s" % name)

    def do_exit(self, args):
        """Exit the program."""
        raise SystemExit

    def do_http(self, args):
        """
        http - Connect a switch through HTTP protocal
        --
        http username@hostname
        --
        """
        if len(args) == 0: print("Command error"); return
        username, host = args.split('@') if '@' in args else ["admin", args]
        password = getpass.getpass('Password: ')
        cli.connect(host)
        if not cli.login(username, password):
            return
        prompt.prompt = '%s@%s # ' % (username, host)

    def do_logout(self, args):
        """Logout current switch"""
        cli.logout()
        cli.close()
        prompt.prompt = '(not connect)> '

    def do_show(self, args):
        if args == "ru" or args == "run":
            cli.showDashboard()
        elif args == "int":
            cli.showPortStatus()
        elif args == "vlan":
            cli.showVlanStatus()
            cli.showVlanPort()

    def do_setinfo(self, args):
        cl.setSystemInfo(input("Switch Name: "), input("Location: "), input("Contact: "))

prompt = Prompt()
prompt.prompt = '(not connect)> '
prompt.cmdloop('HP 1820 wrapper version 1.0')