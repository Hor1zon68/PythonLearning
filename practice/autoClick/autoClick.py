# 改进版
import pyautogui
from time import sleep, time
from pynput import mouse, keyboard
import logging


# 定义一个处理键盘输入的回调函数
# def on_press(key):
#     print('{0} pressed'.format(key))

class AutoClick(object):
    if_break = False
    screen_width = 0
    screen_height = 0

    def __init__(self):
        super(AutoClick, self).__init__()

        pyautogui.PAUSE = 0
        self.setting_logging()
        self.keyboard_mouse_listener_init()

        self.screen_width, self.screen_height = pyautogui.size()
        pass

    def setting_logging(self):
        # debug<info<warning<error<critical
        log_format = 'Time:%(asctime)s - Log_Level:%(levelname)s - Log_Message:%(message)s'
        logging.basicConfig(level=logging.INFO, format=log_format, filename='autoClick.log', filemode='w')
        pass

    def on_press(self, key):  # 监测按键按下的回调函数
        logging.debug('{0} pressed'.format(key))
        pass

    def on_release(self, key):  # 监测按键松开的回调函数
        logging.debug('{0} released'.format(key))
        if key == keyboard.Key.esc:  # 按下esc就退出
            self.if_break = True
            exit(0)
        pass

    def on_click(self, x, y, button, pressed):  # 监测鼠标点击的回调函数
        if button == mouse.Button.left:
            logging.debug('Left button clicked at ({0}, {1})'.format(x, y))
        elif button == mouse.Button.right:
            logging.debug('Right button clicked at ({0}, {1})'.format(x, y))

    def on_scroll(self, x, y, dx, dy):  # 监测滚轮的回调函数
        logging.debug('Scrolled at ({0}, {1}) with {2} and {3}'.format(x, y, dx, dy))
        pass

    def on_move(self, x, y):  # 监测鼠标移动的回调函数
       # logging.debug('Mouse move to ({0}, {1})'.format(x, y))
        pass

    def keyboard_mouse_listener_init(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        mouse_listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll, on_move=self.on_move)
        keyboard_listener.start()  # 非阻断式监听
        mouse_listener.start()
        pass

    def mouse_click(self, click_times, click_left_or_right, click_interval_sec=0.05):
        print('请注意：您需要在5秒内将鼠标移动到您需要连点的地方，然后不要动，等待开始快速连点。')
        sleep(5)
        print('开始点击！')

        start_time = time()
        for i in range(0, click_times):
            x, y = pyautogui.position()
            # click_left_or_right为‘left’或者‘right’
            pyautogui.click(x, y, button=click_left_or_right, interval=0.01)
            sleep(click_interval_sec)
        spend_time = time() - start_time
        input('完成。用时%f秒。' % spend_time)


    def key(self, input_char, input_times, input_interval_sec=0.01):
        print('请在以下支持的按键中挑选您需要的键。')
        for i in pyautogui.KEYBOARD_KEYS:
            print(r'%s' % i, end=' ')

        if input_char in pyautogui.KEYBOARD_KEYS:
            print('请注意，您需要在5秒内切换到需要输入的窗口。')
            sleep(5)
            print('开始工作！')
            start_time = time()
            for i in range(0, input_times):
                pyautogui.press(input_char)
                sleep(input_interval_sec)
            spend_time = time() - start_time
            input('完成。用时%f秒。' % spend_time)
        else:
            input('您输入的字符不属于支持字符，请修改。')


if __name__ == '__main__':
    autoclick = AutoClick()

    # keyboard_listener.join()#阻断式监听
    # 除了最后一个监听器外，其他监听器不能用listener.join()
    # 的方式启动，只能用非阻塞的listener.start()
    # 的方式启动。最后一个监听器则应当以listener.join()
    # 的方式启动，以使程序执行被阻塞，防止程序直接结束。
    try:

        # keyboard_listener.join() 阻塞式

        # 创建键盘监听器，同时监听按下和释放事件

        while True:
            print(1)
            sleep(1)

    except Exception as e:
        print('错误；\n', e)
