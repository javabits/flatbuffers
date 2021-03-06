// automatically generated by the FlatBuffers compiler, do not modify

namespace Testing.KeySearch
{

using System;
using FlatBuffers;

public struct EnumEntry : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static EnumEntry GetRootAsEnumEntry(ByteBuffer _bb) { return GetRootAsEnumEntry(_bb, new EnumEntry()); }
  public static EnumEntry GetRootAsEnumEntry(ByteBuffer _bb, EnumEntry obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public EnumEntry __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public FruitFilter Key { get { int o = __p.__offset(4); return o != 0 ? (FruitFilter)__p.bb.GetInt(o + __p.bb_pos) : 0; } }
  public bool MutateKey(FruitFilter key) { int o = __p.__offset(4); if (o != 0) { __p.bb.PutInt(o + __p.bb_pos, (int)key); return true; } else { return false; } }
  public int Value { get { int o = __p.__offset(6); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)7412; } }
  public bool MutateValue(int value) { int o = __p.__offset(6); if (o != 0) { __p.bb.PutInt(o + __p.bb_pos, value); return true; } else { return false; } }

  public static Offset<EnumEntry> CreateEnumEntry(FlatBufferBuilder builder,
      FruitFilter key = 0,
      int value = 7412) {
    builder.StartObject(2);
    EnumEntry.AddValue(builder, value);
    EnumEntry.AddKey(builder, key);
    return EnumEntry.EndEnumEntry(builder);
  }

  public static void StartEnumEntry(FlatBufferBuilder builder) { builder.StartObject(2); }
  public static void AddKey(FlatBufferBuilder builder, FruitFilter key) { builder.AddInt(0, (int)key, 0); }
  public static void AddValue(FlatBufferBuilder builder, int value) { builder.AddInt(1, value, 7412); }
  public static Offset<EnumEntry> EndEnumEntry(FlatBufferBuilder builder) {
    int o = builder.EndObject();
    return new Offset<EnumEntry>(o);
  }

  public static VectorOffset CreateMySortedVectorOfTables(FlatBufferBuilder builder, Offset<EnumEntry>[] offsets) {
    Array.Sort(offsets, (Offset<EnumEntry> o1, Offset<EnumEntry> o2) => builder.DataBufferp.bb.GetInt(Table.__offset(4, o1.Value, builder.DataBuffer)).CompareTo(builder.DataBufferp.bb.GetInt(Table.__offset(4, o2.Value, builder.DataBuffer))));
    return builder.CreateVectorOfTables(offsets);
  }

  public static EnumEntry? LookupByKey( int bb_pos, VectorOffset fieldDataOffset, FruitFilter key, FruitFilter defaultKeyValue , ByteBuffer bb) {
    int vectorLocation = bb.Length - vectorOffset.Value;
    int span = bb.GetInt(vectorLocation);
    vectorLocation += 4;
    int start = 0;
    while (span != 0) {
      int middle = span / 2;
      int tableOffset = Table.__indirect(vectorLocation + 4 * (start + middle), bb);
      int comp = __p.bb.GetInt(Table.__offset(4, bb.Length - tableOffset, bb)).CompareTo(key);
      if (comp > 0) {
        span = middle;
      } else if (comp < 0) {
        middle++;
        start += middle;
        span -= middle;
      } else {
        return new EnumEntry().__assign(tableOffset, bb);
      }
    }
    return null;
  }
};


}
