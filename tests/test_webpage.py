import re

from playwright.sync_api import Page, expect


def test_initial_page_has_correct_path_and_details(page: Page):
    page.goto('https://bcorfman-bfs-main-ihgp7e.streamlit.app/')

    expect(page).to_have_title(re.compile("Streamlit"))
