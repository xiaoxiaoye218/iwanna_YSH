

from source import tools,setup
from  source.states import main_menu,level
#主函数
def main():
    state_dict={
        'main_menu':main_menu.MainMenu(),
        'level0':level.level0(),
        'level1':level.level1(),
        'level2': level.level2(),
        'level3': level.level3(),
        'level4': level.level4()
    }
    game=tools.Game(state_dict,'main_menu')
    game.run()


if __name__=='__main__':
    main()