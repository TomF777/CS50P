from project import get_disk_partitions, get_cpu_count, get_memory_util
import pytest

def test_get_disk_partitions():
    """
    Assertion must be adjusted according to OS on which the project runs
    """

    assert len(get_disk_partitions()) == 9

def test_get_cpu_count():
    """
    Assertion must be adjusted according to OS on which the project runs
    """

    assert get_cpu_count() == 1


def test_get_memory_util():
    """
    Assertion must be adjusted according to OS on which the project runs
    """

    total, free, used = get_memory_util()
    assert total == pytest.approx(7943,53)
