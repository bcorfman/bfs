from playwright.sync_api import Page, expect


def test_default_solution_path(page: Page):
    page.goto("https://bcorfman-bfs-main-ihgp7e.streamlit.app/")
    expect(
        page.frame_locator("iframe[title=\"streamlitApp\"]").
        get_by_text("Path:")).to_have_text(
            "Path: [(15, 6), (15, 7), (15, 8), (16, 8), (17, 8), (18, 8), "
            "(19, 8), (20, 8), (21, 8), (22, 8), (23, 8), (24, 8), (25, 8), "
            "(26, 8), (27, 8), (28, 8), (29, 8), (30, 8), (31, 8), (32, 8), "
            "(33, 8), (34, 8), (35, 8), (36, 8), (37, 8), (38, 8), (39, 8), "
            "(39, 7), (39, 6), (40, 6), (41, 6), (42, 6), (42, 7), (43, 7), "
            "(44, 7)]")
