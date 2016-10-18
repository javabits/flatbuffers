// automatically generated by the FlatBuffers compiler, do not modify

package KeySearch

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type DoubleEntry struct {
	_tab flatbuffers.Table
}

func GetRootAsDoubleEntry(buf []byte, offset flatbuffers.UOffsetT) *DoubleEntry {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &DoubleEntry{}
	x.Init(buf, n+offset)
	return x
}

func (rcv *DoubleEntry) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *DoubleEntry) Key() float64 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.GetFloat64(o + rcv._tab.Pos)
	}
	return 0.0
}

func (rcv *DoubleEntry) MutateKey(n float64) bool {
	return rcv._tab.MutateFloat64Slot(4, n)
}

func (rcv *DoubleEntry) Value() float64 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.GetFloat64(o + rcv._tab.Pos)
	}
	return 4567.0
}

func (rcv *DoubleEntry) MutateValue(n float64) bool {
	return rcv._tab.MutateFloat64Slot(6, n)
}

func DoubleEntryStart(builder *flatbuffers.Builder) {
	builder.StartObject(2)
}
func DoubleEntryAddKey(builder *flatbuffers.Builder, key float64) {
	builder.PrependFloat64Slot(0, key, 0.0)
}
func DoubleEntryAddValue(builder *flatbuffers.Builder, value float64) {
	builder.PrependFloat64Slot(1, value, 4567.0)
}
func DoubleEntryEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}
