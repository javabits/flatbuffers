# automatically generated by the FlatBuffers compiler, do not modify

# namespace: KeySearch

import flatbuffers

class MasterDict(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMasterDict(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MasterDict()
        x.Init(buf, n + offset)
        return x

    # MasterDict
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MasterDict
    def UbytesEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .UByteEntry import UByteEntry
            obj = UByteEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def UbytesEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def BytesEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ByteEntry import ByteEntry
            obj = ByteEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def BytesEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def BoolEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .BoolEntry import BoolEntry
            obj = BoolEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def BoolEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def ShortEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ShortEntry import ShortEntry
            obj = ShortEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def ShortEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def UshortEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .UShortEntry import UShortEntry
            obj = UShortEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def UshortEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def IntEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .IntEntry import IntEntry
            obj = IntEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def IntEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def UintEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .UIntEntry import UIntEntry
            obj = UIntEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def UintEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def FloatEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FloatEntry import FloatEntry
            obj = FloatEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def FloatEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def LongEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .LongEntry import LongEntry
            obj = LongEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def LongEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def UlongEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ULongEntry import ULongEntry
            obj = ULongEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def UlongEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def DoubleEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .DoubleEntry import DoubleEntry
            obj = DoubleEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def DoubleEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MasterDict
    def StringEntries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .StringEntry import StringEntry
            obj = StringEntry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MasterDict
    def StringEntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def MasterDictStart(builder): builder.StartObject(12)
def MasterDictAddUbytesEntries(builder, ubytesEntries): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(ubytesEntries), 0)
def MasterDictStartUbytesEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddBytesEntries(builder, bytesEntries): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(bytesEntries), 0)
def MasterDictStartBytesEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddBoolEntries(builder, boolEntries): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(boolEntries), 0)
def MasterDictStartBoolEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddShortEntries(builder, shortEntries): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(shortEntries), 0)
def MasterDictStartShortEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddUshortEntries(builder, ushortEntries): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ushortEntries), 0)
def MasterDictStartUshortEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddIntEntries(builder, intEntries): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(intEntries), 0)
def MasterDictStartIntEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddUintEntries(builder, uintEntries): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(uintEntries), 0)
def MasterDictStartUintEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddFloatEntries(builder, floatEntries): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(floatEntries), 0)
def MasterDictStartFloatEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddLongEntries(builder, longEntries): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(longEntries), 0)
def MasterDictStartLongEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddUlongEntries(builder, ulongEntries): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(ulongEntries), 0)
def MasterDictStartUlongEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddDoubleEntries(builder, doubleEntries): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(doubleEntries), 0)
def MasterDictStartDoubleEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictAddStringEntries(builder, stringEntries): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(stringEntries), 0)
def MasterDictStartStringEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MasterDictEnd(builder): return builder.EndObject()