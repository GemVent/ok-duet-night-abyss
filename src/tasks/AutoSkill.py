from qfluentwidgets import FluentIcon
import time
import cv2
import re

from ok import Logger, TaskDisabledException
from src.tasks.BaseCombatTask import BaseCombatTask
from src.tasks.DNAOneTimeTask import DNAOneTimeTask
from src.tasks.CommissionsTask import CommissionsTask

logger = Logger.get_logger(__name__)


class AutoSkill(DNAOneTimeTask, CommissionsTask, BaseCombatTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = FluentIcon.FLAG
        self.name = "自动释放技能"

        self.default_config.update({
            '主画面侦测': True,
            # 添加多次技能释放相关的配置，继承自CommissionsTask
            '启用多次技能释放': False,
            '多次释放次数': 3,
            '多次释放间隔': 0.2,
            '多次释放冷却时间': 8.0,
        })

        self.setup_commission_config()
        keys_to_remove = ["委托手册", "启用自动穿引共鸣", "自动选择首个密函和密函奖励"]
        for key in keys_to_remove:
            self.default_config.pop(key, None)

        self.config_description.update({
            '主画面侦测': '如果不在可操控角色的画面则结束任务',
            '超时时间': '超时后将发出提示',
            '启用多次技能释放': '是否启用短时间内多次释放技能功能',
            '多次释放次数': '短时间内连续释放技能的次数',
            '多次释放间隔': '多次释放之间的间隔时间(秒)',
            '多次释放冷却时间': '多次释放后的冷却时间(秒)',
        })
        
        self.action_timeout = 10
        
    def run(self):
        DNAOneTimeTask.run(self)
        try:
            return self.do_run()
        except TaskDisabledException as e:
            pass
        except Exception as e:
            logger.error('AutoCombatSkill error', e)
            raise

    def do_run(self):
        self.load_char()
        _skill_time = 0
        self.wait_until(self.in_team, time_out=30)
        while True:
            if self.in_team():
                _skill_time = self.use_skill(_skill_time)
            else:
                if self.config.get('主画面侦测', False):
                    self.log_info_notify('任务完成')
                    self.soundBeep()
                    return
            if time.time() - self.start_time >= self.config.get('超时时间', 120):
                self.log_info_notify('任务超时')
                self.soundBeep()
                return
            self.sleep(0.2)
