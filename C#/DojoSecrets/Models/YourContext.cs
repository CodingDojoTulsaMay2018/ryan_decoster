using Microsoft.EntityFrameworkCore;

namespace DojoSecrets.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) {}
        public DbSet<User> Users { get; set; }
        public DbSet<Secret> Secrets { get; set; }
        public DbSet<Like> Likes { get; set; }
    }
}