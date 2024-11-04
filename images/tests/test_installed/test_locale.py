
def test_locale(container, expected):
    output, _ = container.exec(["locale"])
    assert 'LC_ALL=en_US.UTF-8' in output
    assert 'LANG=en_US.UTF-8' in output
    assert 'LANGUAGE=en_US.UTF-8' in output
