import unittest

import core.tasks as tasks
from utils.config import is_message_sending_enabled


class SelectorTests(unittest.TestCase):
    def test_conversation_item_selector_uses_class_selector_so_pinned_items_match(self):
        self.assertEqual(tasks.CONVERSATION_ITEM_SELECTOR, '.conversationConversationItemwrapper')
        self.assertEqual(tasks.CONVERSATION_TITLE_SELECTOR, '.conversationConversationItemtitle')
        self.assertEqual(tasks.CONVERSATION_LIST_SELECTOR, '.conversationConversationListwrapper')
        self.assertEqual(tasks.CHAT_EDITOR_SELECTOR, '.messageEditorimChatEditorContainer')


class MessageSendingGateTests(unittest.TestCase):
    def test_sending_requires_explicit_opt_in(self):
        for value in (None, "", "false", "0", "off", "no"):
            with self.subTest(value=value):
                self.assertFalse(is_message_sending_enabled(value))

    def test_sending_accepts_explicit_true_values(self):
        for value in ("true", "1", "yes", "on", " TRUE "):
            with self.subTest(value=value):
                self.assertTrue(is_message_sending_enabled(value))


if __name__ == '__main__':
    unittest.main()

