import compression.zstd as zstd
import gzip
import time

# Sample data for compression testing
sample_data = b"Python 3.14 brings amazing new features! " * 1000

# Zstandard compression
start_time = time.time()
zstd_compressed = zstd.compress(sample_data, level=3)
zstd_time = time.time() - start_time

# Traditional gzip compression for comparison
start_time = time.time()
gzip_compressed = gzip.compress(sample_data, compresslevel=6)
gzip_time = time.time() - start_time

# Compare results
print(f"Original size: {len(sample_data):,} bytes")
print(f"Zstandard: {len(zstd_compressed):,} bytes ({zstd_time:.4f}s)")
print(f"Gzip: {len(gzip_compressed):,} bytes ({gzip_time:.4f}s)")

# Decompression
decompressed = zstd.decompress(zstd_compressed)
assert sample_data == decompressed

# Advanced usage with custom compression levels
high_compression = zstd.compress(sample_data, level=19)  # Maximum compression
fast_compression = zstd.compress(sample_data, level=1)   # Fastest compression

print(f"High compression: {len(high_compression):,} bytes")
print(f"Fast compression: {len(fast_compression):,} bytes")