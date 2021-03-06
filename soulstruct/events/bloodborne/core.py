import sys
from pathlib import Path

from soulstruct.events.base import BaseEMEVD, BaseEvent, BaseEventArg, BaseInstruction, BaseEventLayers
from soulstruct.events.core import convert_events as convert_events_base
from soulstruct.utilities.core import BinaryStruct

from .constants import ALL_MAPS


class EventLayers(BaseEventLayers):
    STRUCT = BinaryStruct(
        ('two', 'I', 2),
        ('event_layers', 'I'),  # 32-bit bit field
        ('zero', 'Q', 0),
        ('minus_one', 'q', -1),
        ('one', 'Q', 1),
    )


class EventArg(BaseEventArg):
    STRUCT = BinaryStruct(
        ('instruction_line', 'Q'),
        ('write_from_byte', 'Q'),
        ('read_from_byte', 'Q'),
        ('bytes_to_write', 'Q'),
    )


class Instruction(BaseInstruction):
    EventLayers = EventLayers
    INSTRUCTION_ARG_TYPES = {
        2000: {
            0: 'iII', 1: 'iI', 2: 'B', 3: 'B', 4: 'I',
            5: 'B'},
        2001: {},
        2002: {
            1: 'iI', 2: 'iIiBB', 3: 'iIi', 4: 'iIiBBi',
            5: 'iIffifi', 6: 'iIiBBiB', 7: 'iIiB', 8: 'iBB'},
        2003: {
            1: 'iiBB', 2: 'iB', 3: 'iB', 4: 'i',
            5: 'iiiiiii', 6: 'iB', 7: 'iB', 8: 'iiB', 9: 'i',
            10: 'h', 11: 'bihi', 12: 'i', 13: 'iIB', 14: 'BBi',
            15: 'i', 16: 'I', 17: 'IIB', 18: 'iiBBB', 19: 'hh',
            20: 'i', 21: 'B', 22: 'iiB', 23: 'i', 24: 'iii',
            25: 'iiiii', 26: 'iB', 27: 'B', 28: 'i', 29: 'Bb',
            30: 'B', 31: 'iII', 32: 'iI', 33: 'i', 34: 'iiii',
            35: 'ii', 36: 'i', 37: '', 38: '', 39: '',
            40: '', 41: 'iIiiIb', 42: 'iiiI', 43: 'iiiI', 44: 'B',
            45: 'ihhhB', 46: 'hB', 47: 'hhhB', 48: 'iBfi', 49: 'i',
            50: 'i', 51: 'iiiii', 52: 'i', 53: 'ib', 54: 'i'},
        2004: {
            1: 'iB', 2: 'iB', 3: 'iBii', 4: 'iB',
            5: 'iB', 6: 'iiB', 7: 'i', 8: 'iiB', 9: 'iiiiii',
            10: 'iB', 11: 'ii', 12: 'iB', 13: 'ii', 14: 'iiiB',
            15: 'iB', 16: 'i', 17: 'iiB', 18: 'iif', 19: 'ii',
            20: 'i', 21: 'ii', 22: 'ihhiffBB', 23: 'iiiB', 24: 'iiii',
            25: 'iif', 26: 'iBB', 27: 'iBB', 28: 'ii', 29: 'iB',
            30: 'iB', 31: 'iB', 32: 'iiBii', 33: 'ii', 34: 'iBb',
            35: 'iB', 36: 'iii', 37: 'i', 38: 'B', 39: 'iB',
            40: 'iBiii', 41: 'iBii', 42: 'iBiii', 43: 'iB', 44: 'iB',
            45: 'ii', 46: 'B', 47: '', 48: 'iBB', 49: 'ii',
            50: 'if', 51: 'iiiiii', 52: 'i', 53: 'i', 54: 'iB',
            55: 'iiB'},
        2005: {
            1: 'ib', 2: 'i', 3: 'iB', 4: 'iB',
            5: 'iii', 6: 'iiB', 7: 'ii', 8: 'ib', 9: 'iiiiifff',
            10: 'iBBB', 11: 'iih', 12: 'i', 13: 'iB', 14: 'iiiB',
            15: 'i', 16: 'iiii', 17: 'iB'},
        2006: {
            1: 'iB', 2: 'i', 3: 'iiii', 4: 'iii',
            5: 'ii'},
        2007: {
            1: 'ihhif', 2: 'B', 3: 'iB', 4: 'iB',
            5: 'i', 6: 'i', 7: 'i', 8: 'i', 9: 'i'},
        2008: {
            1: 'ii', 2: 'iiiiff', 3: 'BBH'},
        2009: {
            0: 'iii', 1: 'iii', 2: 'iii', 3: 'iiffi', 4: 'i',
            5: 'iiffii', 6: 'B'},
        2010: {
            1: 'BHiii', 2: 'iii', 3: 'iB', 4: 'iB',
            5: 'iB'},
        2011: {
            1: 'iB', 2: 'iB', 3: 'iB'},
        2012: {
            1: 'iB'},
        2013: {
            1: 's', 2: 'IsB', 3: 'I', 4: 'BsB'},
        1000: {
            0: 'Bb', 1: 'BBb', 2: 'BBb', 3: 'B', 4: 'B', 5: 'Bbii',
            6: 'Bbii', 7: 'BBb', 8: 'BBb', 9: 'f',
            101: 'BBb', 103: 'B', 105: 'Bbii', 107: 'BBb'},
        1001: {
            0: 'f', 1: 'i', 2: 'ff', 3: 'ii'},
        1003: {
            0: 'BBi', 1: 'BBBi', 2: 'BBBi', 3: 'BBBii', 4: 'BBBii',
            5: 'Bb', 6: 'Bb', 7: 'BBBB', 8: 'BBBB', 9: 'BBB',
            10: 'BBB', 11: 'BB', 12: 'BB', 13: 'BB', 14: 'BBBB',
            15: 'BBBB', 16: 'BBBB', 101: 'BBBi', 103: 'BBBii',
            105: 'Bb', 107: 'BBBB', 109: 'BBB'},
        1005: {
            0: 'Bi', 1: 'BBi', 2: 'BBi', 101: 'BBi'},
        1014: {
            0: '', 1: '', 2: '', 3: '', 4: '',
            5: '', 6: '', 7: '', 8: '', 9: ''},
        0: {
            0: 'bBb', 1: 'bbii'},
        1: {
            0: 'bf', 1: 'bi', 2: 'bff', 3: 'bii'},
        3: {
            0: 'bBBi', 1: 'bBBii', 2: 'bBii', 3: 'bBiif', 4: 'bBiB',
            5: 'biifhfiBi', 6: 'bb', 7: 'bBi', 8: 'bBBB', 9: 'bI',
            10: 'bBiibi', 11: 'bBBB', 12: 'biBBI', 13: 'biifhfiBi', 14: 'bi',
            15: 'bii', 16: 'bBiB', 17: 'bBB', 18: 'biifhfiBii', 19: 'biifhfiBii',
            20: 'biBBiB', 21: 'bB', 22: 'bB', 23: 'biiB', 24: 'bii',
            25: 'bBii', 26: 'bBb', 27: 'bb', 28: 'bb', 29: 'bBBB'},
        4: {
            0: 'biB', 1: 'bii', 2: 'bibf', 3: 'bib', 4: 'biiB',
            5: 'biiB', 6: 'biiib', 7: 'biB', 8: 'biiB', 9: 'biB',
            10: 'bB', 11: 'bB', 12: 'bB', 13: 'bBI', 14: 'biBi',
            15: 'biB'},
        5: {
            0: 'bBi', 1: 'bii', 2: 'bi', 3: 'bibi'},
        11: {
            0: 'bi', 1: 'bi', 2: 'bi'}
    }
    STRUCT = BinaryStruct(
        ('instruction_class', 'I'),
        ('instruction_index', 'I'),
        ('base_args_size', 'Q'),
        ('first_base_arg_offset', 'i'),
        '4x',
        ('first_event_layers_offset', 'i'),  # unused in BB
        '4x',
    )


class Event(BaseEvent):
    Instruction = Instruction
    EventArg = EventArg
    EVENT_ARG_TYPES = {}
    STRUCT = BinaryStruct(
        ('event_id', 'Q'),
        ('instruction_count', 'Q'),
        ('first_instruction_offset', 'Q'),
        ('event_arg_count', 'Q'),
        ('first_event_arg_offset', 'i'),
        '4x',
        ('restart_type', 'I'),
        '4x',
    )


class EMEVD(BaseEMEVD):
    Event = Event
    GAME_MODULE = sys.modules["soulstruct.events.bloodborne"]
    STRING_ENCODING = 'utf-16le'
    DCX_MAGIC = (68, 76)
    STRUCT = BinaryStruct(
        ('version', '4s', b'EVD\x00'),
        ('bloodborne_marker', 'I', 65280),
        ('unknown', 'I', 204),
        ('file_size_1', 'I'),
        ('event_count', 'Q'),
        ('event_table_offset', 'Q'),
        ('instruction_count', 'Q'),
        ('instruction_table_offset', 'Q'),
        '8x',  # unknown table, unused in all games
        ('unknown_table_offset', 'Q'),
        ('event_layers_count', 'Q'),  # unused in BB
        ('event_layers_table_offset', 'Q'),  # unused in BB
        ('event_arg_count', 'Q'),
        ('event_arg_table_offset', 'Q'),
        ('linked_files_count', 'Q'),
        ('linked_files_table_offset', 'Q'),
        ('base_arg_data_size', 'Q'),
        ('base_arg_data_offset', 'Q'),
        ('packed_strings_size', 'Q'),
        ('packed_strings_offset', 'Q'),
        # No more 4x at the end.
    )

    def compute_base_args_size(self, existing_data_size):
        total_arg_size = sum([e.total_args_size for e in self.events.values()])
        while (existing_data_size + total_arg_size) % 16 != 0:
            total_arg_size += 1  # pad to multiple of 16
        return total_arg_size

    def pad_after_base_args(self, emevd_binary_after_base_args):
        while len(emevd_binary_after_base_args) % 16 != 0:
            emevd_binary_after_base_args += b'\0'  # pad to multiple of 16
        return emevd_binary_after_base_args


def convert_events(output_type, output_directory, input_type=None, input_directory=None, maps=None):
    input_directory = Path(input_directory) if input_directory is not None else Path(__file__.parent) / 'vanilla'
    if not maps:
        maps = ALL_MAPS
    return convert_events_base(
        output_type=output_type, output_directory=output_directory,
        input_directory=input_directory, maps=maps, emevd_class=EMEVD, input_type=input_type)
