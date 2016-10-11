// automatically generated by the FlatBuffers compiler, do not modify

package KeySearch

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type UShortEntry struct {
	_tab flatbuffers.Table
}

func GetRootAsUShortEntry(buf []byte, offset flatbuffers.UOffsetT) *UShortEntry {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &UShortEntry{}
	x.Init(buf, n+offset)
	return x
}

func (rcv *UShortEntry) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *UShortEntry) Key() uint16 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetUint16(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *UShortEntry) MutateKey(n uint16) bool {
	return rcv._tab.MutateUint16Slot(4, n)
}

func (rcv *UShortEntry) Value() uint16 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.GetUint16(o + rcv._tab.Pos)
	}
	return 65535
}

func (rcv *UShortEntry) MutateValue(n uint16) bool {
	return rcv._tab.MutateUint16Slot(6, n)
}

func UShortEntryStart(builder *flatbuffers.Builder) {
	builder.StartObject(2)
}
func UShortEntryAddKey(builder *flatbuffers.Builder, key uint16) {
	builder.PrependUint16Slot(0, key, 0)
}
func UShortEntryAddValue(builder *flatbuffers.Builder, value uint16) {
	builder.PrependUint16Slot(1, value, 65535)
}
func UShortEntryEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}