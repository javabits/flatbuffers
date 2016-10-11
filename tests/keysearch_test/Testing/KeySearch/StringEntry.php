<?php
// automatically generated by the FlatBuffers compiler, do not modify

namespace Testing\KeySearch;

use \Google\FlatBuffers\Struct;
use \Google\FlatBuffers\Table;
use \Google\FlatBuffers\ByteBuffer;
use \Google\FlatBuffers\FlatBufferBuilder;

class StringEntry extends Table
{
    /**
     * @param ByteBuffer $bb
     * @return StringEntry
     */
    public static function getRootAsStringEntry(ByteBuffer $bb)
    {
        $obj = new StringEntry();
        return ($obj->init($bb->getInt($bb->getPosition()) + $bb->getPosition(), $bb));
    }

    public static function StringEntryIdentifier()
    {
        return "FBMD";
    }

    public static function StringEntryBufferHasIdentifier(ByteBuffer $buf)
    {
        return self::__has_identifier($buf, self::StringEntryIdentifier());
    }

    public static function StringEntryExtension()
    {
        return "mdict";
    }

    /**
     * @param int $_i offset
     * @param ByteBuffer $_bb
     * @return StringEntry
     **/
    public function init($_i, ByteBuffer $_bb)
    {
        $this->bb_pos = $_i;
        $this->bb = $_bb;
        return $this;
    }

    public function getKey()
    {
        $o = $this->__offset(4);
        return $o != 0 ? $this->__string($o + $this->bb_pos) : null;
    }

    /**
     * @return int
     */
    public function getValue()
    {
        $o = $this->__offset(6);
        return $o != 0 ? $this->bb->getInt($o + $this->bb_pos) : 7890;
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return void
     */
    public static function startStringEntry(FlatBufferBuilder $builder)
    {
        $builder->StartObject(2);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return StringEntry
     */
    public static function createStringEntry(FlatBufferBuilder $builder, $key, $value)
    {
        $builder->startObject(2);
        self::addKey($builder, $key);
        self::addValue($builder, $value);
        $o = $builder->endObject();
        $builder->required($o, 4);  // key
        return $o;
    }

    /**
     * @param FlatBufferBuilder $builder
     * @param StringOffset
     * @return void
     */
    public static function addKey(FlatBufferBuilder $builder, $key)
    {
        $builder->addOffsetX(0, $key, 0);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @param int
     * @return void
     */
    public static function addValue(FlatBufferBuilder $builder, $value)
    {
        $builder->addIntX(1, $value, 7890);
    }

    /**
     * @param FlatBufferBuilder $builder
     * @return int table offset
     */
    public static function endStringEntry(FlatBufferBuilder $builder)
    {
        $o = $builder->endObject();
        $builder->required($o, 4);  // key
        return $o;
    }
}