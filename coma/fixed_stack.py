#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:47:20 2021

# 고정 길이 스택 클래스 FixedStack 구현하기

@author: ssac6
"""
from typing import Any

class FixedStack:
    
    # 예외 처리 클래스 Empty : 스택이 비어 있으면 예외처리 
    class Empty(Exception): 
        pass
    
    # 예외 처리 클래스 Full : 스택이 가득 차 있으면 예외처리
    class Full(Exception):
        pass
    
    # 초기화 함수
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
        
    # 쌓여 있는 데이터 갯수 알아내기 : 포이터를 그대로 반환
    def __len__(self) -> int:
        return self.ptr
        
    # 스택이 비어 있는지를 판단하는 함수
    def is_empty(self) -> bool:
        return self.ptr <= 0
        
    # 스택이 가득 차 있는지를 판단하는 함수
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    # 데이터를 푸시하는 함수 : 스택에 데이터를 추가
    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
        
    # 데이터를 팝하는 함수 : 스택의 꼭대기에서 데이터를 꺼내서 반환
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    # 데이터를 들여다보는 함수 : 스택의 꼭대기 데이터를 들여다봄
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    # 스택의 모든 데이터를 삭제하는 함수
    def clear(self) -> None:
        self.ptr = 0
        
    # 데이터를 검색하는 함수
    def find(self, value: Any) -> Any:
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    # 데이터 갯수를 세는 함수 
    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    
    # 데이터가 포함되어 있는지 판단하는 함수 
    def __contains__(self, value: Any) -> bool:
        return self.count(value)
    
    # 스택의 모든 데이터를 출력하는 함수 
    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
