#!/usr/bin/env python3
""" Module documentation """
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """doc func"""
    listDelays = []
    for _ in range(n):
        listDelays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*listDelays))
