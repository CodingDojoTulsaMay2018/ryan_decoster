using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace DojoSecrets.Models
{
    public class User
    {
        [Key]
        public int Id { get; set; }
        public string First_Name { get; set; }
        public string Last_Name { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public DateTime Created_At { get; set; }
        public DateTime Updated_At { get; set; }
        public List<Secret> Secrets { get; set; }
        public List<Like> Likes { get; set; }
        public User()
        {
            Created_At = DateTime.Now;
            Updated_At = DateTime.Now;
            Secrets = new List<Secret>();
            Likes = new List<Like>();
        }
    }
    public class Secret
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "Secret field must not be empty.")]
        [MinLength(5, ErrorMessage = "Secrets be at least 5 characters.")]
        public string Content { get; set; }
        public DateTime Created_At { get; set;}
        public DateTime Updated_At { get; set;}
        public int UserId { get; set; }
        public User Creator { get; set; }
        public List<Like> Likes { get; set; }
        public Secret()
        {
            Created_At = DateTime.Now;
            Updated_At = DateTime.Now;
            Likes = new List<Like>();
        }
    }
    public class Like
    {
        [Key]
        public int Id { get; set; }
        public int SecretId { get; set; }
        public Secret Secret { get; set; }
        public int UserId { get; set; }
        public User LikedUser { get; set; }
    }
}