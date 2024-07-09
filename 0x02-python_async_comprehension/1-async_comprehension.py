#!/usr/bin/env python3
""" Module documentation """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Func doc"""
    return [random async for random in async_generator()]
