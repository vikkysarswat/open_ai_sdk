import React, { useEffect, useState } from "react";

interface NewsCard {
  title: string;
  description: string;
  image: string;
  url: string;
  publishedAt: string;
  source: string;
}

const ChatKitPanel: React.FC = () => {
  const [news, setNews] = useState<NewsCard[]>([]);

  useEffect(() => {
    // Mocked data first — replace with your Render backend later
    setNews([
      {
        title: "AI Revolutionizes Stock Market Predictions",
        description:
          "New generative AI models are now outperforming analysts in predicting short-term stock trends.",
        image: "https://source.unsplash.com/800x400/?stock,ai",
        url: "#",
        publishedAt: "Oct 17, 2025",
        source: "Bloomberg AI",
      },
      {
        title: "ChatGPT Apps SDK Ushers a New Era of AI Interfaces",
        description:
          "Developers can now build dynamic UI cards directly inside ChatGPT using the new SDK tools.",
        image: "https://source.unsplash.com/800x400/?technology,news",
        url: "#",
        publishedAt: "Oct 16, 2025",
        source: "TechCrunch",
      },
    ]);
  }, []);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-gray-800 text-center">
        📰 AI News Dashboard
      </h1>

      <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {news.map((item, i) => (
          <div
            key={i}
            className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300"
          >
            <img
              src={item.image}
              alt={item.title}
              className="w-full h-48 object-cover"
            />
            <div className="p-4">
              <h2 className="font-semibold text-lg mb-2 text-gray-800">
                {item.title}
              </h2>
              <p className="text-gray-600 text-sm mb-3 line-clamp-3">
                {item.description}
              </p>
              <div className="flex justify-between items-center text-xs text-gray-500">
                <span>{item.publishedAt}</span>
                <span>{item.source}</span>
              </div>
              <a
                href={item.url}
                className="text-blue-600 text-sm font-medium hover:underline mt-2 inline-block"
                target="_blank"
              >
                Read full article →
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChatKitPanel;
