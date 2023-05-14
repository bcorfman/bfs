import os

import pytest
from playwright.async_api import Page, expect


@pytest.mark.system
async def test_default_solution_path(page: Page):
    url = os.environ.get('STREAMLIT_DEPLOYMENT_URL')
    if url:
        await page.goto(url)
    else:
        await page.goto("https://bcorfman-bfs-main-ihgp7e.streamlit.app/")
    locator = page.frame_locator("iframe[title=\"streamlitApp\"]")
    element = await locator.get_by_text("Path:")
    assert element is not None
    await expect(element).to_contain_text(
        "[(15, 6), (15, 7), (15, 8), (16, 8), (17, 8), (18, 8), (19, 8), "
        "(20, 8), (21, 8), (22, 8), (23, 8), (24, 8), (25, 8), (26, 8), "
        "(27, 8), (28, 8), (29, 8), (30, 8), (31, 8), (32, 8), (33, 8), "
        "(34, 8), (35, 8), (36, 8), (37, 8), (38, 8), (39, 8), (39, 7), "
        "(39, 6), (40, 6), (41, 6), (42, 6), (42, 7), (43, 7), (44, 7)]")


@pytest.mark.system
async def test_start_node_outside_map_boundary(page: Page):
    url = os.environ.get('STREAMLIT_DEPLOYMENT_URL')
    if url:
        await page.goto(url)
    else:
        await page.goto("https://bcorfman-bfs-main-ihgp7e.streamlit.app/")

    locator = page.frame_locator("iframe[title=\"streamlitApp\"]")
    await locator.get_by_role("spinbutton", name="X:").first.fill("30")
    await locator.get_by_role("spinbutton", name="X:").first.press("Tab")
    await locator.get_by_role("spinbutton", name="Y:").first.fill("5")
    await locator.get_by_role("spinbutton", name="Y:").first.press("Tab")
    element = locator.get_by_text("Path:")
    assert element is not None
    await expect(element).to_contain_text(
        "No solution found. Outside map boundary.")


@pytest.mark.system
async def test_start_node_one_line_above_map_boundary(page: Page):
    url = os.environ.get('STREAMLIT_DEPLOYMENT_URL')
    if url:
        await page.goto(url)
    else:
        await page.goto("https://bcorfman-bfs-main-ihgp7e.streamlit.app/")
    locator = page.frame_locator("iframe[title=\"streamlitApp\"]")
    await locator.get_by_role("spinbutton", name="X:").first.fill("26")
    await locator.get_by_role("spinbutton", name="X:").first.press("Tab")
    await locator.get_by_role("spinbutton", name="Y:").first.fill("6")
    await locator.get_by_role("spinbutton", name="Y:").first.press("Tab")
    element = locator.get_by_text("Path:")
    assert element is not None
    await expect(element).to_contain_text(
        "No solution found. Outside map boundary.")
