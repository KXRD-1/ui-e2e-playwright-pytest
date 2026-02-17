import os
import re
import pytest
from playwright.sync_api import Playwright
from ui_e2e.config import BASE_URL

ARTIFACTS_DIR = os.path.abspath("artifacts")


def _safe(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", name)
    return name[:150]


@pytest.fixture()
def context(playwright: Playwright, request):
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)

    browser = playwright.chromium.launch(headless=True)
    ctx = browser.new_context(
        base_url=BASE_URL,
        record_video_dir=os.path.join(ARTIFACTS_DIR, "video"),
        record_video_size={"width": 1280, "height": 720},
        viewport={"width": 1280, "height": 720},
    )

    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield ctx

    test_name = _safe(request.node.name)
    trace_path = os.path.join(ARTIFACTS_DIR, "trace", f"{test_name}.zip")
    os.makedirs(os.path.dirname(trace_path), exist_ok=True)
    ctx.tracing.stop(path=trace_path)

    ctx.close()
    browser.close()


@pytest.fixture()
def page(context, request):
    p = context.new_page()
    yield p

    if request.node.rep_call.failed:
        test_name = _safe(request.node.name)
        screenshot_path = os.path.join(ARTIFACTS_DIR, "screenshots", f"{test_name}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        p.screenshot(path=screenshot_path, full_page=True)

    p.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
